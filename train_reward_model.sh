python train_reward_model.py \
    --model "nghuyong/ernie-3.0-base-zh" \
    --train_path "data/reward_datasets/sentiment_analysis/train.tsv" \
    --dev_path "data/reward_datasets/sentiment_analysis/dev.tsv" \
    --save_dir "checkpoints/reward_model/sentiment_analysis" \
    --img_log_dir "logs/reward_model/sentiment_analysis" \
    --img_log_name "ERNIE Reward Model" \
    --batch_size 32 \
    --max_seq_len 128 \
    --learning_rate 1e-5 \
    --valid_steps 50 \
    --logging_steps 10 \
    --num_train_epochs 10 \
    --device "cuda:0"