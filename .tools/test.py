import requests

def get_component(repo):
  print("get component")
  component = "main"
  if "linuxdeepin/" in repo:
    component = "dde"
  else:
    rawurl = "https://raw.githubusercontent.com/{repo}/master/debian/deepin/workflows.yml".format(repo=repo)
    res = requests.get(rawurl.replace("+", "%2B"))
    if res.status_code == 200:
      #print(res.content)
      if "deepin:Develop:community" in str(res.content):
        component = "community"
    else:
      print("Warn: get workflows.yml content failed!!!")
      component = "community"
  return component

print(get_component("deepin-community/nexttrace"))
print(get_component("linuxdeepin/nexttrace"))
print(get_component("deepin-community/xorg"))
