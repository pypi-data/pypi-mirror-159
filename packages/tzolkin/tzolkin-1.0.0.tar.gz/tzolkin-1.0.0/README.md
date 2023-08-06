# `Tzolk'in`: Scheduling for Humans™

`tsolkin` is a python scheduler based on
`cron`, `schedule`, `snaptime`, and `maya`.

## F.A.Q.

### What's with the name?

The Tzolk'in is a mayan calander.
I named it that because it's a scheduler based on `maya`,
the excellent datatime library by Kenneth Reitz.

### What does `tzolkin` do differently?

It's designed for maximum flexibility and built to be human interpretable.

All the core elements are abstract classes with minimal interfaces.

Need some weird asynchronous behavior, or to ensure consistency across a bunch
of remote nodes? Write a `Schedule`.

Want to schedule something for every time there's penumbral lunar eclipse over
Old Carthage, or the first day of every prime numbered Gregorian year?
Write a `TimeSet`.

Need to trigger something weird? If you can fit it in a python function, it'll
work as a `Job`.

### Why did you make this?

I needed it for another project. I started out using `schedule`, but it quickly
became clear that I needed something more flexible and extensible.

### Why not improve `schedule`?

My particular use cases would have required pretty dramatic changes,
and looking at the contribution rules (in particular the requirement that it
work for python2, and the requirement that it not use external libraries)
for `schedule` I decided it was not going to be very plausible.

In addition, I wanted more flexible fluent building, and native first class
support for jobs that run only once.

### Why not improve `python-crontab`?

The goals of python-crontab are a little different. I wanted to focus on
scheduling within python (not just running bash jobs). I wanted to support
scheduling singleton jobs, as above. And I wanted something more readable.

