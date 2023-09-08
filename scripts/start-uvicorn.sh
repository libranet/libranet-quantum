#!/bin/bash
uvicorn --factory libranet_qiskit.api:create_app --reload
