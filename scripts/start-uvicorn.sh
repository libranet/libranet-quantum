#!/bin/bash
uvicorn --factory libranet_quantum.api:create_app --reload
