/*
 * This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0.  If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/.
 *
 * Copyright 2008-2019 MonetDB B.V.
 */

extern FILE* embedded_stdout;
extern FILE* embedded_stderr;

#define exit(status) ((void) (status))
#undef assert
#define NDEBUG 1
#define assert(ignore) ((void) 0)
#undef stdout
#define stdout embedded_stdout
#undef stderr
#define stderr embedded_stderr

#ifdef HAVE_EMBEDDED_R
#define srand(seed) ((void) (seed))
extern int embedded_r_rand(void);
#define rand embedded_r_rand
#endif

#undef PTRFMT
#undef PTRFMTCAST

#define PTRFMT "%p"
#define PTRFMTCAST (void *)
