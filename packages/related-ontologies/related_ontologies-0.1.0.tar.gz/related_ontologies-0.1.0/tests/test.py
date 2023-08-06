import os
import yaml
import time
import errno
import pandas as pd
from related_ontologies.related import generateRelatedOntologies


def load_config(file):
    print(f'Loading {file}...')
    with open(file, "r") as f:
        configurations = yaml.safe_load(f)
        print('Done.\n')
        return configurations


if __name__ == "__main__":
    print("Beginning test...")

    config_file = r'C:\Users\Justin\PycharmProjects\mimic-iv-dash\config.yaml'
    if os.path.exists(config_file):
        print('Configuration file found.')
        config = load_config(r'C:\Users\Justin\PycharmProjects\mimic-iv-dash\config.yaml')
    else:
        raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), config_file)

    PATH_loinc = config['loinc']['location']
    PATH_data = config['directories']['data']
    df_loinc = pd.read_csv(r'C:\Users\Justin\PycharmProjects\mimic-iv-dash\demo-data\LoincTableCore.csv', dtype=object)
    df_loinc = df_loinc[df_loinc['CLASSTYPE'] == str(1)]
    df_loinc.drop(df_loinc[df_loinc.STATUS != 'ACTIVE'].index, inplace=True)
    df_loinc.drop(['CLASSTYPE', 'STATUS', 'EXTERNAL_COPYRIGHT_NOTICE', 'VersionFirstReleased', 'VersionLastChanged'],
                  axis=1,
                  inplace=True)
    print(f"LOINC codes (CLASSTYPE=1, Laboratory Terms Class) loaded and processed.\n")

    loinc_dict = pd.Series(df_loinc.LONG_COMMON_NAME.values, index=df_loinc.LOINC_NUM.values).to_dict()
    df_loinc_new = pd.DataFrame(
        {'LOINC_NUM': list(loinc_dict.keys()), 'LONG_COMMON_NAME': list(loinc_dict.values())})
    df_loinc_new = df_loinc_new.reset_index().rename(columns={"index": "id"})

    query = list(loinc_dict.values())[0]
    choices = list(loinc_dict.values())
    method = 'partial_ratio'

    related = generateRelatedOntologies(query, choices, method)

    df_related_score = pd.DataFrame(related[1:], columns=['LONG_COMMON_NAME', 'partial_ratio'])
    df_related = df_loinc_new[df_loinc_new['LONG_COMMON_NAME'].isin([i[0] for i in related[1:]])]
    df_data = df_related.merge(df_related_score, on='LONG_COMMON_NAME')
    df_data = df_data.sort_values(by=['partial_ratio'], ascending=False)
