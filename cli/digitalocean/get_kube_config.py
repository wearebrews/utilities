import requests
import json
import unicodedata
import re
import argparse


def get_token_from_file(file="token.txt"):
    with open(file, "r") as bear:
        return "Bearer " + bear.read()

#r = requests.get("https://api.digitalocean.com/v2/kubernetes/clusters", headers = {"Content-Type": "application/json", "Authorization": token )
#r = requests.get("https://api.digitalocean.com/v2/kubernetes/clusters/062a09f5-242f-4bf8-b7f6-6d033025041c/kubeconfig", headers = {"Content-Type": "application/json", "Authorization": token } )
# print(r.content)

def list_clusters(token):
    r = requests.get("https://api.digitalocean.com/v2/kubernetes/clusters", headers = {"Content-Type": "application/json", "Authorization": token} )
    if r.status_code != 200:
        print("Invalid token")
        return None
    return r.json()

def get_clusters_user_input(clusters):
    for i in range(len(clusters)):
        print(clusters['kubernetes_clusters'][i]['name'])
    return int(input("Select cluster? (0,1,2,..) "))
    

def get_id(index:int, clusters):
    cluster_id = clusters['kubernetes_clusters'][index]['id']
    return cluster_id

def write_to_file(config, f):
    with open("kubeconfig.yaml","w") as config: 
            config.write(config)


def get_kube_config(argv):
    parser = argparse.ArgumentParser(description="Get kubernetes config file")
    parser.add_argument("-o", "--out")
    parser.add_argument("--tokenfile", default="token.txt")
    parser.add_argument("--token")
    args = parser.parse_args(argv[1:])
    print(args)


    token = args.token
    if token == None:
        token = get_token_from_file(args.tokenfile)

    clusters = list_clusters(token)
    if clusters == None:
        #No valid clusters
        return

    clusterNumb = len(clusters['kubernetes_clusters'])
    if clusterNumb == 0:
        print("No clusters")
        return
    i = get_clusters_user_input(clusters)
    url = "https://api.digitalocean.com/v2/kubernetes/clusters/" + get_id(i, clusters) + "/kubeconfig"
    c = requests.get(url, headers = {"Content-Type": "application/json", "Authorization": token } )

    if args.out != None:
        write_to_file(str(c.text), args.out)
    else:
        print(str(c.text))


