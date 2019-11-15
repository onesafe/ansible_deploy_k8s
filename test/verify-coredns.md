```bash
[root@wyp-k8s01 ~]# kubectl create -f my-nginx.yaml
deployment.extensions/my-nginx created

[root@wyp-k8s01 ~]# kubectl expose deploy my-nginx
service/my-nginx exposed
```

```bash
[root@wyp-k8s01 ~]# kubectl create -f dnsutils-ds.yml
service/dnsutils-ds created
```

```bash
[root@wyp-k8s01 ~]# kubectl exec -it dnsutils-ds-8qxsx bash
root@dnsutils-ds-8qxsx:/# ls
bin  boot  dev  etc  home  lib  lib64  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
root@dnsutils-ds-8qxsx:/# cat /etc/resolv.conf
nameserver 10.254.0.2
search default.svc.cluster.local svc.cluster.local cluster.local 4pd.io
options ndots:5
root@dnsutils-ds-8qxsx:/# nslookup kubernetes
Server:		10.254.0.2
Address:	10.254.0.2#53

Name:	kubernetes.default.svc.cluster.local
Address: 10.254.0.1

root@dnsutils-ds-8qxsx:/# nslookup www.baidu.com
Server:		10.254.0.2
Address:	10.254.0.2#53

Non-authoritative answer:
*** Can't find www.baidu.com: No answer

root@dnsutils-ds-8qxsx:/# nslookup my-nginx
Server:		10.254.0.2
Address:	10.254.0.2#53

Name:	my-nginx.default.svc.cluster.local
Address: 10.254.74.184

root@dnsutils-ds-8qxsx:/# nslookup kube-dns.kube-system.svc.cluster
Server:		10.254.0.2
Address:	10.254.0.2#53

Non-authoritative answer:
*** Can't find kube-dns.kube-system.svc.cluster: No answer

root@dnsutils-ds-8qxsx:/# nslookup kube-dns.kube-system.svc
Server:		10.254.0.2
Address:	10.254.0.2#53

Name:	kube-dns.kube-system.svc.cluster.local
Address: 10.254.0.2

root@dnsutils-ds-8qxsx:/# nslookup kube-dns.kube-system.svc.cluster.local
Server:		10.254.0.2
Address:	10.254.0.2#53

Non-authoritative answer:
*** Can't find kube-dns.kube-system.svc.cluster.local: No answer

root@dnsutils-ds-8qxsx:/# nslookup kube-dns.kube-system.svc.cluster.local.
Server:		10.254.0.2
Address:	10.254.0.2#53

Name:	kube-dns.kube-system.svc.cluster.local
Address: 10.254.0.2

root@dnsutils-ds-8qxsx:/# nslookup kube-dns.kube-system.svc.cluster.local
Server:		10.254.0.2
Address:	10.254.0.2#53

Non-authoritative answer:
*** Can't find kube-dns.kube-system.svc.cluster.local: No answer

root@dnsutils-ds-8qxsx:/# nslookup kube-dns.kube-system.svc
Server:		10.254.0.2
Address:	10.254.0.2#53

Name:	kube-dns.kube-system.svc.cluster.local
Address: 10.254.0.2

root@dnsutils-ds-8qxsx:/# exit
```