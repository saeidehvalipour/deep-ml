from typing import Tuple

def early_stopping(val_losses: list[float], patience: int, min_delta: float) -> Tuple[int, int]:
    # Edge case
    if not val_losses:
        return (-1, -1)

    best_loss = val_losses[0]
    best_epoch = 0
    wait = 0  # how many consecutive epochs without a "real" improvement

    for epoch in range(1, len(val_losses)):
        loss = val_losses[epoch]

        # Improvement is only counted if loss decreases by MORE than min_delta
        if best_loss - loss > min_delta:
            best_loss = loss
            best_epoch = epoch
            wait = 0
        else:
            wait += 1
            if wait >= patience:
                return (epoch, best_epoch)

    # If we never triggered early stop, "stop" at the last epoch
    return (len(val_losses) - 1, best_epoch)
