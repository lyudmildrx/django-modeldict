from django.core import signals
import time
import gargoyle
gg = gargoyle.gargoyle
status = gg.is_active('my_favourity_switchy')
while True:
    print gg.is_active('my_favourity_switchy'), gg._last_checked_for_remote_changes, gg.local_cache_has_expired()
    new_status = gg.is_active('my_favourity_switchy')
    if new_status != status:
        print 'Z' * 88
        break

    status = new_status
    signals.request_finished.send(1)
    time.sleep(0.5) # Increase sleep time to see issue happening more and more rarely
