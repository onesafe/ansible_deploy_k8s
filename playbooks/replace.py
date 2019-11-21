#!/bin/env python
# -*- coding: utf-8 -*-

import yaml
from jinja2 import Environment, FileSystemLoader

yml_file_path = "../inventory/group_vars/all/all.yml"
prepare_etc_host_file_path = "roles/prepare/templates/hosts"
etcd_csr_j2_file_path = "roles/etcd/files/etcd-csr.json.j2"
etcd_csr_file_path = "roles/etcd/files/etcd-csr.json"
controller_manager_j2_file_path = "roles/controller-manager/files/kube-controller-manager-csr.json.j2"
controller_manager_file_path = "roles/controller-manager/files/kube-controller-manager-csr.json"
kube_scheduler_j2_file_path = "roles/kube-scheduler/files/kube-scheduler-csr.json.j2"
kube_scheduler_file_path = "roles/kube-scheduler/files/kube-scheduler-csr.json"
kubernetes_j2_file_path = "roles/apiserver/files/kubernetes-csr.json.j2"
kubernetes_file_path = "roles/apiserver/files/kubernetes-csr.json"
kube_nginx_j2_file_path = "roles/kube-nginx/templates/kube-nginx.conf.j2"
kube_nginx_file_path = "roles/kube-nginx/templates/kube-nginx.conf"

def get_ips_names():
    with open(yml_file_path, "r") as f:
        data = yaml.safe_load(f.read())
    
        node_ips = data.get("NODE_IPS").split(",")
        node_ips = [node.strip() for node in node_ips]

        node_names = data.get("NODE_NAMES").split(",")
        node_names = [node.strip() for node in node_names]
        print node_ips
        print node_names

        ips_names = dict(zip(node_ips,node_names))
        return ips_names

def prepare_etc_host(ips_names):
    with open(prepare_etc_host_file_path, "w") as f:
        print ips_names
        for ip, name in ips_names.items():
            print ip, name
            f.write(ip + " " + name + "\n")

def generate_etcd_csr(ips_names):
    env = Environment(loader=FileSystemLoader("."))
    template = env.get_template(etcd_csr_j2_file_path)
    content = template.render(ips=ips_names.keys())
    print content
    with open(etcd_csr_file_path, "w") as f:
        f.write(content)

def generate_controller_manager_csr(ips_names):
    env = Environment(loader=FileSystemLoader("."))
    template = env.get_template(controller_manager_j2_file_path)
    content = template.render(ips=ips_names.keys())
    print content
    with open(controller_manager_file_path, "w") as f:
        f.write(content)

def generate_kube_scheduler_csr(ips_names):
    env = Environment(loader=FileSystemLoader("."))
    template = env.get_template(kube_scheduler_j2_file_path)
    content = template.render(ips=ips_names.keys())
    print content
    with open(kube_scheduler_file_path, "w") as f:
        f.write(content)

def generate_kubernetes_csr(ips_names):
    env = Environment(loader=FileSystemLoader("."))
    template = env.get_template(kubernetes_j2_file_path)
    content = template.render(ips=ips_names.keys())
    print content
    with open(kubernetes_file_path, "w") as f:
        f.write(content)

def generate_kube_nginx_conf(ips_names):
    env = Environment(loader=FileSystemLoader("."))
    template = env.get_template(kube_nginx_j2_file_path)
    content = template.render(ips=ips_names.keys())
    print content
    with open(kube_nginx_file_path, "w") as f:
        f.write(content)

def main():
    ips_names = get_ips_names()
    prepare_etc_host(ips_names)
    generate_etcd_csr(ips_names)
    generate_controller_manager_csr(ips_names)
    generate_kube_scheduler_csr(ips_names)
    generate_kubernetes_csr(ips_names)
    generate_kube_nginx_conf(ips_names)


if __name__ == "__main__":
    main()