# -*- mode: python; coding: utf-8; -*-
# Copyright 2010 Cristian Esquivias, Kenny Meyer

# This file is part of django-memorize.

# django-memorize is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation, either version 3 of the License, or (at your
# option) any later version.

# django-memorize is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License
# for more details.

# You should have received a copy of the GNU General Public License
# along with django-memorize.  If not, see <http://www.gnu.org/licenses/>.

def interval(repition, rating, easy_factor=2.5):
    ef = easy_factor + (0.1 - (5 - rating) * (0.08 + (5 - rating) * 0.02))
    ef = ef if ef >= 1.3 else 1.3

    if rating < 3:
        return 1, ef
    if repition == 1:
        return 1, ef
    if repition == 2:
        return 6, ef

    days, ef = interval(repition-1, rating, easy_factor)
    days *= easy_factor
    return days, ef

# vim: ai ts=4 sts=4 et sw=4
