import requests, typer, os, json, sys

app = typer.Typer()
api = os.environ.get('BLECON_API', 'https://api.blecon.net')
key = os.environ.get('BLECON_APIKEY')
if not key:
    print("Error: Please specify the BLECON_APIKEY environment variable")
    sys.exit(1)

@app.command()
def show(
        account_id,
        device_id):
    r = requests.get(api + "/devices/{}?account={}".format(device_id, account_id),
                      headers={"Authorization":str(key)})
    print(json.dumps(r.json(), indent=4, sort_keys=True))

@app.command()
def update(
        account_id: str,
        device_id: str,
        model: str = typer.Option("", help="Set model of device"),
        network_id: str = typer.Option("", help="Set network of device"),
        description: str = typer.Option("", help="Set description of device"),
        request_connection: str = typer.Option("", help="Set request_connection flag of device"),
        ap_lock: str = typer.Option("", help="Force use of specific access point")):

    settings = {}
    for opt in ['model', 'description', 'network_id', 'request_connection', 'ap_lock']:
        if locals().get(opt):
            settings.update({"{}".format(opt): locals().get(opt)})

    # allow setting of ap_lock to empty value
    if type(ap_lock) == str:
        settings.update({"ap_lock": ap_lock})

    print(settings)
    r = requests.post(api + "/devices/{}?account={}".format(device_id, account_id),
                      json=settings,
                      headers={"Authorization":str(key)})
    print(r.content)

@app.command()
def connect(device_id: str, model: str, public_key: str, network_id: str):
    print('NOT_IMPLEMENTED')

@app.command()
def disconnect(device_id: str):
    print('NOT_IMPLEMENTED')
