from langserve import RemoteRunnable

remote_chain = RemoteRunnable("http://localhost:8000/chain/")
