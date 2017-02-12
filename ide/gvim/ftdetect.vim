ftdetect.vim = [
	win32: $USERPROFILE/vimfiles/ftdetect/Y.vim
	unix: ~/.vim/ftdetect/Y.vim
]

ftdetect.vim = [
" Language: syntax/bI
" Maintainer: (c) AUTHOR, all rights reserved

au BufNewFile,BufRead *.src set filetype=Y
au BufNewFile,BufRead log.log set filetype=Y
au BufNewFile,BufRead ram.log set filetype=Y
]