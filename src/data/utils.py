def save_df_to_csv(df, dst_fn):
    if not dst_fn.parent.is_dir():
        dst_fn.parent.mkdir(parents=True)

    df.to_csv(dst_fn, index=False)

    return
