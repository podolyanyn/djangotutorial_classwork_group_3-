import requests, time

for i in range(5):
    start = time.time()

    # res = requests.get("http://127.0.0.1:8000/polls/detail/" + str(i))
    # res = requests.get("http://127.0.0.1:8000/polls/request_to_nbu") #


    print(f'res {i} = {res.text}')
    print(f'time = {time.time() - start}')

