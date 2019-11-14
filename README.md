# 使用ansible部署kubernetes

## 依赖
* `ansible 2.8.5`

## 修改主机名和IP
* `inventory/hosts`
* `inventory/group_vars/all/all.yml`
* `playbooks/roles/prepare/templates/hosts` 
* `playbooks/roles/etcd/files/etcd-csr.json`
* `playbooks/roles/kube-nginx/templates/kube-nginx.conf`

## 升级内核 (Centos7 自带的内核使用k8s有一些bug)
`ansible-playbook -i inventory/hosts playbooks/kernel.yml`

## 使用
`ansible-playbook -i inventory/hosts playbooks/site.yml`
