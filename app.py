from flask import Flask, jsonify
import docker

'''
docker inspector writing for sometimes, that your project up on server
and you need to know, what is your configuration over there 

you can get list of containers that run, and see config environment with get with ID

'''
app = Flask(__name__)
client = docker.from_env()


@app.route("/")
def container_list():
    """
    at this route you have list of container
    :return: {"container id" : "dojo0233923", "container name" : "docker inspector"};
    """
    con_list = list()
    for container in client.containers.list():
        con_list.append({"Container id": container.id, "Container name": container.name})
        print(con_list)
    return jsonify(con_list)


@app.route("/<con_id>")
def inspect_container(con_id):
    """
    API for inspect of your container
    :param con_id:
    :return: name, env, path and another ...
    """
    inspect_value = client.api.inspect_container(con_id)
    con_ins = jsonify(inspect_value['Config'])
    return con_ins


if __name__ == '__main__':
    app.run(debug=True)
