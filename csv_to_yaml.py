import csv
import yaml

def csv_to_yaml(csv_file, yaml_file):
    data = []
    with open(csv_file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)  # Read CSV as dictionaries
        for row in reader:
            data.append(row)

    with open(yaml_file, 'w') as yamlfile:
        match yaml_file:
            case text if 'vs' in text:
               yamlfile.write('virtual_servers:\n')
            case text if 'pool' in text:
               yamlfile.write('pools:\n')

        yaml.dump(data, yamlfile, default_flow_style=False) # default_flow_style=False for block format


if __name__ == "__main__":
    files = [["vs.csv","vars_file_vs.yaml"],["pools.csv","vars_file_pool.yaml"]]
    for file in files:
        source, dest = file
        csv_to_yaml(source, dest)
