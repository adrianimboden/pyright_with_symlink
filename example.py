#/usr/bin/env python3

import symlinked.bar
import orig.bar

orig.bar.foo()
symlinked.bar.foo()