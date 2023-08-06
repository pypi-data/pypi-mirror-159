import json

import numpy as np
import scipy.stats

try:
    import sklearn.metrics
except ImportError:
    pass


def metric_mse(yp, yt):
    return np.sum((yp - yt) ** 2) / yp.shape[0]


def metric_rmse(yp, yt):
    return metric_mse(yp, yt) ** 0.5


def metric_mae(yp, yt):
    return np.sum(np.abs(yp - yt)) / yp.shape[0]


def metric_rhop(yp, yt):
    return scipy.stats.pearsonr(yp, yt)[0]


def metric_rhor(yp, yt):
    return scipy.stats.spearmanr(yp, yt).correlation


def metric_auc(yp, yt):
    return sklearn.metrics.roc_auc_score(yt, yp)


def metric_auc_ovr(yp, yt):
    return sklearn.metrics.roc_auc_score(yt, yp, multi_class="ovr")


def metric_auc_ovo(yp, yt):
    return sklearn.metrics.roc_auc_score(yt, yp, multi_class="ovo")


def metric_acc(yp, yt):
    return 1.0 - np.sum(np.heaviside(np.abs(yp - yt) - 0.5, 0.0)) / len(yt)


def metric_mcc(yp, yt):
    return sklearn.metrics.matthews_corrcoef(yt, yp)


def metric_prec(yp, yt):
    return sklearn.metrics.precision_score(yt, yp)


def metric_rec(yp, yt):
    return sklearn.metrics.recall_score(yt, yp)


def metric_r2(yp, yt):
    return sklearn.metrics.r2_score(yt, yp)


def metric_sup(yp, yt):
    return np.max(np.abs(yp - yt))


def metric_bal(yp, yt):
    return 0.5 * metric_mae(yp, yt) + 0.25 * metric_rmse(yp, yt) + 0.25 * metric_sup(yp, yt)


class Accumulator(object):
    eval_map = {
        "mae": metric_mae,
        "mse": metric_mse,
        "rmse": metric_rmse,
        "rhop": metric_rhop,
        "rhor": metric_rhor,
        "auc": metric_auc,
        "auc_ovo": metric_auc_ovo,
        "auc_ovr": metric_auc_ovr,
        "acc": metric_acc,
        "mcc": metric_mcc,
        "rec": metric_rec,
        "prec": metric_prec,
        "r2": metric_r2,
        "sup": metric_sup,
        "bal": metric_bal,
    }
    select_best = {
        "mae": "smallest",
        "mse": "smallest",
        "rmse": "smallest",
        "rhop": "largest",
        "rhor": "largest",
        "auc": "largest",
        "auc_ovo": "largest",
        "auc_ovr": "largest",
        "acc": "largest",
        "mcc": "largest",
        "rec": "largest",
        "prec": "largest",
        "r2": "largest",
        "sup": "smallest",
        "bal": "smallest",
    }

    @classmethod
    def select(cls, metric):
        return cls.select_best[metric]

    def score(self, metric, *args, **kwargs):
        return self.eval_map[metric](*args, **kwargs)

    def __init__(self, jsonfile=None, metric=None, metrics=None):
        self.yp_map = {}
        self.yt_map = {}
        self.metric = metric
        self.metrics = metrics
        if jsonfile is not None:
            self.load(jsonfile)
        return

    def __getitem__(self, key):
        return np.array(self.yp_map[key]), np.array(self.yt_map[key])

    def append(self, channel, yp, yt):
        if channel not in self.yp_map:
            self.yp_map[channel] = []
            self.yt_map[channel] = []
        self.yp_map[channel] = self.yp_map[channel] + list(yp)
        self.yt_map[channel] = self.yt_map[channel] + list(yt)
        return

    def evaluate(self, channel, metric=None, bootstrap=0):
        if metric is None:
            metric = self.metric
        if len(self.yp_map[channel]) < 1:
            return np.nan
        if bootstrap == 0:
            return (
                Accumulator.eval_map[metric](
                    np.array(self.yp_map[channel]), np.array(self.yt_map[channel])
                ),
                0.0,
            )
        else:
            v = []
            n = len(self.yp_map[channel])
            yp = np.array(self.yp_map[channel])
            yt = np.array(self.yt_map[channel])
            for r in range(bootstrap):
                re = np.random.randint(0, n, size=(n,))
                v.append(Accumulator.eval_map[metric](yp[re], yt[re]))
            return np.mean(v), np.std(v)

    def evaluateNull(self, channel, metric, n_samples):
        if len(self.yp_map[channel]) < 1:
            return np.nan
        z = []
        for i in range(n_samples):
            yp_null = np.array(self.yp_map[channel])
            yt_null = np.array(self.yt_map[channel])
            np.random.shuffle(yp_null)
            z.append(Accumulator.eval_map[metric](yp_null, yt_null))
        z = np.sort(np.array(z))
        return z

    def evaluateAll(self, metrics=None, bootstrap=0, log=None, match=None):
        if metrics is None:
            metrics = self.metrics
        res = {}
        if match is None:
            channels_iter = sorted(self.yp_map)
        else:
            channels_iter = filter(lambda cd: cd.startswith(match), sorted(self.yp_map))
        for channel in channels_iter:
            res[channel] = {}
            metric_logs = []
            for metric in metrics:
                v, dv = self.evaluate(channel, metric, bootstrap=bootstrap)
                res[channel][metric] = v
                res[channel][metric + "_std"] = dv
                if log:
                    metric_logs.append((metric, v, dv))
            if log:
                (
                    log
                    << "  %-14s "
                    % (
                        str(channel)[0:6] + ".." + str(channel)[-6:]
                        if len(str(channel)) > 14
                        else str(channel)
                    )
                    << log.flush
                )
                for metric, v, dv in metric_logs:
                    log << "%s=%+1.4e +- %+1.4e" % (metric, v, dv) << log.flush
                log << log.endl
        return res

    def save(self, jsonfile):
        json.dump(
            {"yp_map": self.yp_map, "yt_map": self.yt_map},
            open(jsonfile, "w"),
            indent=1,
            sort_keys=True,
        )
        return

    def load(self, jsonfile):
        data = json.load(open(jsonfile))
        self.yp_map = data["yp_map"]
        self.yt_map = data["yt_map"]
        return
