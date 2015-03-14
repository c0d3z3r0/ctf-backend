#!/bin/bash
./bootstrap.sh
tar -cf $(date +ctf_backend_%d-%m-%Y--%H-%M.tar) html components vendor
