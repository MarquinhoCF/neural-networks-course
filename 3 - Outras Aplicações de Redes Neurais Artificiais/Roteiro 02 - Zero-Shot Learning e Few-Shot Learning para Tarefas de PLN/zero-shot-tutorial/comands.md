```bash
llama-server \
    --hf-repo Qwen/Qwen3-8B-GGUF \
    --hf-file Qwen3-8B-Q6_K.gguf \
    --n-gpu-layers 10 \
    --threads 16 \
    --ctx-size 4096 \
    --port 8765
```