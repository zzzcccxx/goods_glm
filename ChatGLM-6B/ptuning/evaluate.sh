PRE_SEQ_LEN=64
CHECKPOINT=1000step_e3lr-chatglm-6b-pt-64-5e-3
STEP=800

CUDA_VISIBLE_DEVICES=0 python3 main.py \
    --do_predict \
    --validation_file /root/autodl-tmp/my_data/input/test.json \
    --test_file /root/autodl-tmp/my_data/input/test.json \
    --overwrite_cache \
    --prompt_column content \
    --response_column summary \
    --model_name_or_path /root/autodl-tmp/chatglm_6b \
    --ptuning_checkpoint ./output/$CHECKPOINT/checkpoint-$STEP \
    --output_dir ./output/$CHECKPOINT \
    --overwrite_output_dir \
    --max_source_length 40 \
    --max_target_length 20 \
    --per_device_eval_batch_size 1 \
    --predict_with_generate \
    --pre_seq_len $PRE_SEQ_LEN \
    # --quantization_bit 4
