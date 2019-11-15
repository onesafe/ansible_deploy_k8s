```bash
[root@wyp-k8s01 ~]# kubectl create -f nginx-ds.yml
```

```bash
[root@wyp-k8s01 ~]# kubectl get pods  -o wide|grep nginx-ds
nginx-ds-5w62q   1/1     Running   0          8m8s   172.30.224.2   wyp-k8s03   <none>           <none>
nginx-ds-dkxp9   1/1     Running   0          8m8s   172.30.248.2   wyp-k8s02   <none>           <none>
nginx-ds-mtmkx   1/1     Running   0          8m8s   172.30.24.2    wyp-k8s01   <none>           <none>
```

```bash
[root@wyp-k8s01 ~]# ping -c 1 172.30.224.2
PING 172.30.224.2 (172.30.224.2) 56(84) bytes of data.
64 bytes from 172.30.224.2: icmp_seq=1 ttl=63 time=0.616 ms

--- 172.30.224.2 ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 0.616/0.616/0.616/0.000 ms
```

```bash
[root@wyp-k8s01 ~]# ping -c 1 172.30.248.2
PING 172.30.248.2 (172.30.248.2) 56(84) bytes of data.
64 bytes from 172.30.248.2: icmp_seq=1 ttl=63 time=0.627 ms

--- 172.30.248.2 ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 0.627/0.627/0.627/0.000 ms
```

```bash
[root@wyp-k8s01 ~]# ping -c 1 172.30.24.2
PING 172.30.24.2 (172.30.24.2) 56(84) bytes of data.
64 bytes from 172.30.24.2: icmp_seq=1 ttl=64 time=0.110 ms

--- 172.30.24.2 ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 0.110/0.110/0.110/0.000 ms
```

```bash
[root@wyp-k8s01 ~]# kubectl get svc |grep nginx-ds
nginx-ds     NodePort    10.254.233.182   <none>        80:32452/TCP   9m26s
```


```bash
[root@wyp-k8s01 ~]# curl -s 10.254.233.182
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
<style>
    body {
        width: 35em;
        margin: 0 auto;
        font-family: Tahoma, Verdana, Arial, sans-serif;
    }
</style>
</head>
<body>
<h1>Welcome to nginx!</h1>
<p>If you see this page, the nginx web server is successfully installed and
working. Further configuration is required.</p>

<p>For online documentation and support please refer to
<a href="http://nginx.org/">nginx.org</a>.<br/>
Commercial support is available at
<a href="http://nginx.com/">nginx.com</a>.</p>

<p><em>Thank you for using nginx.</em></p>
</body>
</html>
```

```bash
[root@wyp-k8s01 ~]# curl -s 172.27.129.70:32452
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
<style>
    body {
        width: 35em;
        margin: 0 auto;
        font-family: Tahoma, Verdana, Arial, sans-serif;
    }
</style>
</head>
<body>
<h1>Welcome to nginx!</h1>
<p>If you see this page, the nginx web server is successfully installed and
working. Further configuration is required.</p>

<p>For online documentation and support please refer to
<a href="http://nginx.org/">nginx.org</a>.<br/>
Commercial support is available at
<a href="http://nginx.com/">nginx.com</a>.</p>

<p><em>Thank you for using nginx.</em></p>
</body>
</html>
```


