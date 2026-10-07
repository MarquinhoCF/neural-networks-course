# Iniciar servidor com modelo DeepSeek

```bash
llama-server \
    --hf-repo unsloth/DeepSeek-R1-Distill-Qwen-1.5B-GGUF \
    --hf-file DeepSeek-R1-Distill-Qwen-1.5B-Q4_K_M.gguf \
    --n-gpu-layers 99 \
    --threads 16 \
    --host 127.0.0.1 \
    --port 9999
```