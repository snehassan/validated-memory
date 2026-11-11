#!/bin/bash
# Start the agent model server. Usage: GPU=2 bash scripts/serve.sh
# Check nvidia-smi first and pick a GPU with ~20GB free.
MODEL_PATH=${MODEL_PATH:-/local/tmp/c_snehah/qwen7b}
GPU=${GPU:-2}
CUDA_VISIBLE_DEVICES=$GPU vllm serve "$MODEL_PATH" \
  --served-model-name Qwen/Qwen2.5-Coder-7B-Instruct \
  --generation-config vllm \
  --gpu-memory-utilization ${MEM:-0.9} \
  --max-model-len 4096 \
  --max-num-seqs 32 \
  --port 8471
