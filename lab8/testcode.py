lst = [
    new_time_span(
        new_time(new_hour(13), new_minute(00)), 
        new_time(new_hour(15), new_minute(20))),
    new_time_span(
        new_time(new_hour(10), new_minute(15)), 
        new_time(new_hour(12), new_minute(00)))
]
seq = new_time_span_seq(lst)
sp = new_time_span(
new_time(new_hour(7), new_minute(12)),
    new_time(new_hour(19), new_minute(25))
)
ts = tss_plus_span(seq, sp)

# fix sorting if needed

#    def chronolog(spans: List[TimeSpan]):
#        if not spans:
#            return []
#        elif isinstance(spans, List[TimeSpan]):
            #return 