#!/bin/bash

read -p "Commit description: " desc

git add agg_todo.py && \
git add -u && \
git commit -m "$desc" && \
git push origin main
