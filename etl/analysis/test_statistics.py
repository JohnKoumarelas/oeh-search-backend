import pyelasticsearch as pyes
#es = pyes.ElasticSearch(["http://localhost:9200", "http://hostname1:9200"])  ## don't accidentally type Elasticsearch, the class from the other two modules
es = pyes.ElasticSearch(["http://localhost:9200"])  ## don't accidentally type Elasticsearch, the class from the other two modules

def test():

    schema = es.get_mapping()  ## python dict with the map of the cluster
    # print(schema)

    indices_full_list = schema.keys()
    just_indices = [index for index in indices_full_list if
                    not index.startswith(".")]  ## remove the objects created by marvel, e.g. ".marvel-date"

    print(just_indices)

if __name__ == '__main__':
    test()