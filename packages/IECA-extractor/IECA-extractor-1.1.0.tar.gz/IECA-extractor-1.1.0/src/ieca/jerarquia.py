import copy
import os
import sys
import requests
import pandas as pd
import itertools
import numpy as np
import logging

pd.set_option('mode.chained_assignment', None)

fmt = '[%(asctime)-15s] [%(levelname)s] %(name)s: %(message)s'
logging.basicConfig(format=fmt, level=logging.INFO, stream=sys.stdout)


class Jerarquia:
    """Estructura de datos para manejar las jerarquias encontradas dentro
    de las consultas del IECA, es necesario hacer una petición HTTP para expandir la jerarquia
    y traernos los valores para generar las listas de código que usaremos en SDMX.

    Args:
        jerarquia (:class:`Diccionario`): Información resumida de la jerarquia obtenida en una consulta anterior.
        configuracion_global (:class:`Diccionario`): Configuración común a todas la ejecución.
        actividad (:class:`Cadena de Texto`): Nombre de la actividad.
    Attributes:
        id_jerarquia (:class:`Cadena de Texto`): concatenación del alias y el código de la jerarquia.
        metadatos (:class:`Diccionario`): Metainformación de la jerarquia con los siguientes campos clave:

            - url
            - cod (Codificación)
            - des (Descripción)
            - position (En desuso)
            - order (En desuso)
            - alias (Las jerarquias pueden tener distintos datos, usamos estos alias para concretizarlos)
            - levels (En desuso)
        datos (:class:`pandas:pandas.DataFrame`): La jerarquia en un cuadro de datos que posteriormente puede ser
            exportada a .CSV para importarse en SDMX.
        """

    def __init__(self, jerarquia, configuracion_global, actividad):
        self.configuracion_global = configuracion_global
        self.actividad = actividad
        self.metadatos = jerarquia
        self.id_jerarquia = self.metadatos["alias"] + '-' + self.metadatos['cod']
        self.logger = logging.getLogger(f'{self.__class__.__name__} [{self.id_jerarquia}]')

        self.datos = self.solicitar_informacion_jerarquia()
        self.datos_sdmx = []
        self.nombre = self.metadatos["alias"][2:-2]
        self.logger.info('Extrayendo lista de código')

    def convertir_jerarquia_a_dataframe(self, datos_jerarquia):
        """Transforma el diccionario con los datos de la jerarquia a formato tabular, borrando los valores con Código
        duplicado además de añadir el valor **_Z**.

        Returns:
            datos (:class:`pandas:pandas.DataFrame`): La jerarquia en un cuadro de datos.
         """
        self.logger.info('Transformando Jerarquias')
        data = [datos_jerarquia['data']]
        propiedades_jerarquia = self.configuracion_global['propiedades_jerarquias']

        def recorrer_arbol_recursivamente(datos_jerarquia):
            datos_nivel_actual = [[jerarquia[propiedad] for propiedad in propiedades_jerarquia]
                                  for jerarquia in datos_jerarquia]

            es_ultimo_nivel_rama = np.all(
                [jerarquia['children'] == [] or jerarquia['isLastLevel'] for jerarquia in datos_jerarquia])
            if es_ultimo_nivel_rama:
                return datos_nivel_actual

            return datos_nivel_actual + list(itertools.chain(
                *[recorrer_arbol_recursivamente(jerarquia['children']) for jerarquia in datos_jerarquia]))

        datos_jerarquia = recorrer_arbol_recursivamente(data)
        datos_jerarquia.append(['_Z', 'No aplica', 'No aplica', 'No aplica', 'null', 'null'])

        jerarquia_df = pd.DataFrame(datos_jerarquia, columns=[propiedad.upper() for propiedad in propiedades_jerarquia],
                                    dtype='string')

        jerarquia_df.replace('null', '', inplace=True)
        jerarquia_df.drop_duplicates('COD', keep='first', inplace=True)
        self.logger.info('Jerarquia transformada')

        return jerarquia_df

    def guardar_datos(self):
        """Accion que guarda la jerarquia en formato .CSV de dos formas:

                - Con el Còdigo de BADEA (No admitido por nuestro framework de SDMX)
                - Sin el código de BADEA (Admitido por nuestro framework de SDMX)

            La salida de la lista de código para importar en SDMX se deshará de los valores de las jerarquias
            que no han sido utilizados en la consulta.

         """
        directorio = os.path.join(self.configuracion_global['directorio_jerarquias'], self.actividad)
        directorio_original = os.path.join(directorio, 'original')
        directorio_sdmx = os.path.join(directorio, 'sdmx')

        if not os.path.exists(directorio_original):
            os.makedirs(directorio_original)

        if not os.path.exists(directorio_sdmx):
            os.makedirs(directorio_sdmx)
        self.logger.info('Almacenando datos Jerarquia')
        columnas = ['ID', 'COD', 'NAME', 'DESCRIPTION', 'PARENTCODE', 'ORDER']
        columnas_sdmx = ['ID', 'NAME', 'DESCRIPTION', 'PARENTCODE', 'ORDER']

        datos = copy.deepcopy(self.datos)
        datos.columns = columnas
        self.datos_sdmx = mapear_jerarquia(datos[columnas_sdmx], 'D_' + self.nombre + '_0',
                                           self.configuracion_global[
                                               'directorio_mapas_dimensiones']) if self.nombre in \
                                                                                   self.configuracion_global[
                                                                                       'dimensiones_a_mapear'] else \
            datos[columnas_sdmx]

        datos.to_csv(f'{os.path.join(directorio_original, self.id_jerarquia)}.csv', sep=';', index=False)
        self.datos_sdmx.to_csv(f'{os.path.join(directorio_sdmx, self.id_jerarquia)}.csv', sep=';', index=False)
        self.logger.info('Jerarquia Almacenada')

    def solicitar_informacion_jerarquia(self):
        """Realiza la petición HTTP a la API si la jerarquía no se encuentra en nuestro directorio local,
        automáticamente se convierte la jerarquia a dataframe haciendo uso de
        :attr:`src.jerarquia.Jerarquia.convertir_jerarquia_a_dataframe`.

        Returns:
            datos (:class:`pandas:pandas.DataFrame`): La jerarquia en un cuadro de datos.
         """
        directorio_csv = os.path.join(self.configuracion_global['directorio_jerarquias'], self.actividad, 'original',
                                      self.id_jerarquia + '.csv')
        datos = None
        try:
            self.logger.info('Buscando el CSV de la jerarquia en local')
            with open(directorio_csv, 'r', encoding='utf-8') as csv_file:
                datos = pd.read_csv(csv_file, sep=';', dtype='string')
                self.logger.info('CSV leido correctamente')
        except Exception as e:
            self.logger.warning('No se ha encontrado el fichero %s', directorio_csv)
            self.logger.warning('Excepción: %s', e)
            self.logger.info('Iniciando peticion a la API del IECA')
            datos = self.convertir_jerarquia_a_dataframe(requests.get(self.metadatos['url']).json())
            self.logger.info('Petición API Finalizada')

        finally:
            if datos is not None:
                self.logger.info('Datos alcanzados correctamente')
            else:
                self.logger.warning('No hay información disponible')
        return datos


def mapear_jerarquia(df, dimension, directorio_mapas_dimensiones):
    directorio_mapa = os.path.join(directorio_mapas_dimensiones, dimension)
    df_mapa = pd.read_csv(directorio_mapa, sep=',', dtype='string')

    if 'IGNORE_ON_CL' not in df_mapa.columns:
        df_mapa['IGNORE_ON_CL'] = False
        df_mapa.to_csv(directorio_mapa, sep=',',index=False)

    df.loc[:, 'IGNORE_ON_CL'] = \
        df.merge(df_mapa, how='left', left_on='ID', right_on='SOURCE')['IGNORE_ON_CL'].copy(deep=True)

    df.drop(df.loc[df['IGNORE_ON_CL'] == 'True'].index, inplace=True)

    df.drop('IGNORE_ON_CL', inplace=True, axis=1)

    df.loc[:, 'ID'] = \
        df.merge(df_mapa, how='left', left_on='ID', right_on='SOURCE')['TARGET'].copy(deep=True)
    df.loc[:, 'PARENTCODE'] = \
        df.merge(df_mapa, how='left', left_on='PARENTCODE', right_on='SOURCE')['TARGET'].copy(deep=True)

    return df[df['ID'].notna()]
