import requests
import json
import unicodedata
import re


def getBearer():
    with open("token.txt", "r") as bear:
        return "Bearer " + bear.read()

#r = requests.get("https://api.digitalocean.com/v2/kubernetes/clusters", headers = {"Content-Type": "application/json", "Authorization": token )
#r = requests.get("https://api.digitalocean.com/v2/kubernetes/clusters/062a09f5-242f-4bf8-b7f6-6d033025041c/kubeconfig", headers = {"Content-Type": "application/json", "Authorization": token } )
# print(r.content)

def listClusters():
    token = getBearer()
    r = requests.get("https://api.digitalocean.com/v2/kubernetes/clusters", headers = {"Content-Type": "application/json", "Authorization": token} )
    return r.json()
    


def getID(index):
    clusters = listClusters()
    cluster_id = clusters['kubernetes_clusters'][int(index)]['id']
    print(cluster_id)
    return cluster_id


def getKubeconfig():
    token = getBearer()
    clusters = listClusters()
    clusterNumb = len(clusters['kubernetes_clusters'])
    for i in range(0,clusterNumb):
        print(clusters['kubernetes_clusters'][i]['name'])
    i = input("Hvilkent cluster vil du ha configfilen til? (0,1,2,..) ")
    url = "https://api.digitalocean.com/v2/kubernetes/clusters/" + getID(i) + "/kubeconfig"
    c = requests.get(url, headers = {"Content-Type": "application/json", "Authorization": token } )
    with open("kubeconfig.yaml","w") as config: 
            config.write(str(c.text))



getKubeconfig()


