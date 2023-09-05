PRE_SEQ_LEN=64
LR=5e-3

CUDA_VISIBLE_DEVICES=0 python3 main.py \
    --do_train \
    --train_file /root/autodl-tmp/my_data/input/shuffle_train.json \
    --validation_file /root/autodl-tmp/my_data/input/test.json \
    --prompt_column content \
    --response_column summary \
    --overwrite_cache \
    --model_name_or_path /root/autodl-tmp/chatglm_6b \
    --output_dir output/1000step_e3lr-chatglm-6b-pt-$PRE_SEQ_LEN-$LR \
    --overwrite_output_dir \
    --max_source_length 40 \
    --max_target_length 20 \
    --per_device_train_batch_size 1 \
    --per_device_eval_batch_size 1 \
    --gradient_accumulation_steps 16 \
    --predict_with_generate \
    --max_steps 1000 \
    --logging_steps 10 \
    --save_steps 200 \
    --learning_rate $LR \
    --pre_seq_len $PRE_SEQ_LEN
    # --quantization_bit 4
