# Using `invoke` as library
# http://docs.pyinvoke.org/en/stable/concepts/library.html

from invoke import Collection, Program

from . import dev, docker, git, helm, py


ns = Collection()
ns.add_collection(dev)
ns.add_collection(docker.ns)
ns.add_collection(git.ns)
ns.add_collection(helm.ns)
ns.add_collection(py.ns)


main = Program(namespace=ns, version="0.0.1a2")
