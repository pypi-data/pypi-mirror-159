import sys
import re
from numpy import result_type
import pandas as pd
import logging

from tqdm import tqdm

from .track import Track
from .utils import *

import hook


class CELlinker():
    def __init__(self, ref_file_path="ref_corpus/CEL_meta_new.csv", log=True):
        self.database = pd.read_csv(ref_file_path)
        self.process_reference()
        self.log = log

    def process_reference(self):

        self.database = self.database.fillna("N/A")

        # clean the movements
        movements = self.database["composition-movements_or_sections"].apply(parse_movements)
        self.database[['movements_num', 'movements_name']] = pd.DataFrame(movements.tolist())
        
        # clean the catalogue numbers

        return 

    def process_input(self, record):
        """standarize the record input for query"""
        
        # spotify crawled data
        track = Track(record.track,
                        composer = record.track_artists.split("/")[0])

        return track

    def query_composition(self, record):
        """query the track information and return the most likely composition

        Args:
            record.title: track title
            record.composer: 

        Returns:
            composition: row in the reference dataframe

            (if composition not found then return 0)
        """

        # filter by composer
        database_composer = self.database[self.database['composer-openopus_name'] == record.composer]
        
        if len(database_composer) == 0:
            return None

        key, catalog_number, work_number = parse_title_info(record.title)

        # filter by catalog number
        composition = database_composer[database_composer['composition-catalogue_number'].str.contains(catalog_number+r"(?:'| |/)")]
        # filter by work number (No.) given that multiple works under one catalog number
        composition_work = composition[composition['composition-catalogue_number'].str.contains(work_number+r"(?:'| |/)")]

        if len(composition) == 1:
            return composition
        elif len(composition_work) == 1:
            return composition_work
        elif len(composition_work) >= 2:
            # TODO
            return None
        else:
            # no catalog number, search all for similarity. 
            database_composer["similarity"] = database_composer.apply(lambda x: similarity(x, record), axis=1)
            database_composer = database_composer.sort_values(by=["similarity"], ascending=False)

            # if "Pictures at an Exhibition dedicated to Viktor Hartman" in record.title:
            #     hook()

            THR = 0.72
            if database_composer.iloc[0].similarity < THR:
                return None
            else:

                return database_composer.iloc[0]
             
    
    def query_movement(self, composition, record):
        
        return 1


    def query(self, record):
        
        composition = self.query_composition(record)

        if composition is not None:
            formated_match = format_match(composition, record)
            print(formated_match)
            # rlogger.info(formated_match)
            return self.query_movement(composition, record)
        else:
            rlogger.info(f"+++> Not found: {record.title}")
            return 0

    def batch_query(self, records_file_path):
        records = pd.read_csv(records_file_path)

        founded_count = 0
        for idx, record in tqdm(records.iterrows()):
            record = self.process_input(record)
            founded_count += self.query(record)
        
        print(f"founded {founded_count} / {len(records)}")

            # if idx == 100:
            #     hook()

        return 
    

    
if __name__ == "__main__":

    # logger = logging.getLogger()
    # logger.setLevel(logging.INFO)

    rlogger = logging.getLogger()
    rlogger.setLevel(logging.INFO)

    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setLevel(logging.INFO)

    file_handler = logging.FileHandler('results.log')
    file_handler.setLevel(logging.INFO)

    rlogger.addHandler(file_handler)
    # logger.addHandler(stdout_handler)


    linker = CELlinker()
    # track = Track("Violin Sonata in A Major, Op. 162, D. 574 ""Grand Duo"": III. Andantino (Live)", composer="Franz Schubert")
    # composition = linker.query(track)
    linker.batch_query("spotify_50pianists_records.csv")
