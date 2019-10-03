#!/usr/bin/env nextflow
echo true

cheers = Channel.from 'Bonjour', 'Ciao', 'Hello', 'Hola'

process sayHello {
  // container "ubuntu:latest"
  container "quay.io/biocontainers/seurat-scripts:0.0.5--r34_1"
  cpus 1
  memory '512 MB'
  input: 
    val x from cheers
  script:
    """
    echo '$x world!'
    """
}


