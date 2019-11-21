# 使用ansible部署kubernetes

## Dashboard
![Dashboard](images/dashboard.jpg)

## 依赖
* `ansible 2.8.5`
* `python 2.7 (jinja2, PyYAML)`

## 前提条件（修改下面文件的主机名和IP）
* `inventory/hosts`
* `inventory/group_vars/all/all.yml`

## 部署集群 (v1.14.2版本的kubernetes)
`ansible-playbook -i inventory/hosts playbooks/site.yml`

##### 需要关注
* 下载kubernetes-server-linux-amd64.tar.gz文件慢的话（playbooks/roles/master），可以注释掉roles/master/tasks/main.yml，手动先下载上传到节点/opt/k8s/work/路径下

## 查看集群服务状态
`ansible-playbook -i inventory/hosts playbooks/site.yml --tags "status"`

## 清理集群
在同一套环境里面部署多次的话，可以先清理集群

`ansible-playbook -i inventory/hosts playbooks/clean.yml`

## 升级内核 (Centos7 自带的内核使用k8s有一些bug)
`ansible-playbook -i inventory/hosts playbooks/kernel.yml`
