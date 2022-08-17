# =========================================================================
# Type definition
# =========================================================================

from cal_abstraction import *
from cal_output import *
# Define the type somehow...  The initial "" is simply here as a placeholder.
#TimeSpanSeq = ""
TimeSpanSeq = NamedTuple("TimeSpanSeq", [("spans", List[TimeSpan])])

# =========================================================================
#  Function implementations
# =========================================================================

# Implement these functions!  Also determine if you need *additional* functions.

# new_time_span(start: Time, end: Time) -> TimeSpan:
def new_time_span_seq(spans: List[TimeSpan] = None) -> TimeSpanSeq:
    """Create and return a new TimeSpanSeq for the given TimeSpans"""
    if spans is None:
        # If we use [] as a default value above, then every call to this function will
        # use the *same* list as a default value.  Instead we must use None as
        # a value, and if something empty is provided, we create a *new* list each time.
        spans = []
    else:
        ensure_type(spans, List[TimeSpan])

    return TimeSpanSeq(spans)


def tss_is_empty(tss: TimeSpanSeq) -> bool:
    """ Return true iff the given timespanseq has no TimeSpans """
    ensure_type(tss, TimeSpanSeq)
    return not tss.spans


def tss_plus_span(tss: TimeSpanSeq, ts: TimeSpan) -> TimeSpanSeq:
    """
    Returns TimeSpanSeq, where the given TimeSpan 
    has been added in its proper position.
    """
    ensure_type(ts, TimeSpan)
    ensure_type(tss, TimeSpanSeq)

    def add_ts(tss: TimeSpanSeq, ts: TimeSpan): #List[span]
        if not tss or isinstance(tss, TimeSpanSeq) and tss_is_empty(tss):
            return [ts]
        elif time_precedes(
            ts_start(ts), ts_start(tss[0][0])
        ):
            return [ts] + tss[0]
        else:
            return tss[0] + add_ts(tss[1:], ts)

    return new_time_span_seq(add_ts(tss, ts))


def tss_iter_spans(tss: TimeSpanSeq):
    """To be used as `for span in cd_iter_spans(tss)"""
    ensure_type(tss, TimeSpanSeq)
    for TimeSpan in tss.spans:
        yield TimeSpan


def show_time_spans(tss: TimeSpanSeq):
    """Print the TimeSpanSeq, one TimeSpan per line."""
    for TimeSpan in tss.spans:
        show_ts(TimeSpan)
        print()



# Keep only time spans that satisfy pred.
# You do not need to modify this function.
def tss_keep_spans(tss, pred):
    result = new_time_span_seq()
    for span in tss_iter_spans(tss):
        if pred(span):
            result = tss_plus_span(result, span)

    return result



