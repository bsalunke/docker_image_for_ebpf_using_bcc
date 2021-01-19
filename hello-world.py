#!/usr/bin/python
from bcc import BPF

prog = """
int kprobe__sys_clone(void *ctx) {
    bpf_trace_printk("Hello world\\n");
    return 0;
}
"""

b = BPF(text=prog)
#b.attach_kprobe(event="sys_clone", fn_name="hello")
b.trace_print()

# This prints out a trace line every time the clone system call is called

# If you rename hello() to kprobe__sys_clone() you can delete the b.attach_kprobe() line, because bcc can work
# out what event to attach this to from the function name.
