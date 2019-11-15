# 使用ansible部署kubernetes

## 依赖
* `ansible 2.8.5`

## 修改主机名和IP
* `inventory/hosts`
* `inventory/group_vars/all/all.yml`
* `playbooks/roles/prepare/templates/hosts` 
* `playbooks/roles/etcd/files/etcd-csr.json`
* `playbooks/roles/kube-nginx/templates/kube-nginx.conf`
* `playbooks/roles/controller-manager/files/kube-controller-manager-csr.json`
* `playbooks/roles/kube-scheduler/files/kube-scheduler-csr.json`

## 升级内核 (Centos7 自带的内核使用k8s有一些bug)
`ansible-playbook -i inventory/hosts playbooks/kernel.yml`

## 部署集群
`ansible-playbook -i inventory/hosts playbooks/site.yml`

## 清理集群
`ansible-playbook -i inventory/hosts playbooks/clean.yml`

## 注意事项
* `主机名字符串需要符合下面要求 (e.g. 'example.com', regex used for validation is '[a-z0-9]([-a-z0-9]*[a-z0-9])?(\\.[a-z0-9]([-a-z0-9]*[a-z0-9])?)*')`

* `下载kubernetes-server-linux-amd64.tar.gz文件，网速比较慢的话，可以注释掉roles/master/tasks/main.yml，手动先下载上传到节点/opt/k8s/work/路径下`

## 手动执行的命令
### 对kubelet server执行approve csr (playbooks/roles/kubelet)
`/opt/k8s/bin/kubectl get csr | grep Pending | awk '{print $1}' | xargs /opt/k8s/bin/kubectl certificate approve`
