"dein Scripts-----------------------------
if &compatible
  set nocompatible               " Be iMproved
endif

" Required:
set runtimepath+=/home/alvazir/.local/share/dein/repos/github.com/Shougo/dein.vim

" Required:
if dein#load_state('/home/alvazir/.local/share/dein')
  call dein#begin('/home/alvazir/.local/share/dein')

  " Let dein manage dein
  " Required:
  call dein#add('/home/alvazir/.local/share/dein/repos/github.com/Shougo/dein.vim')

  " Add or remove your plugins here:
  call dein#add('Valloric/YouCompleteMe')
  call dein#add('vim-airline/vim-airline')
  call dein#add('davidhalter/jedi-vim')
  call dein#add('w0rp/ale')
  call dein#add('plytophogy/vim-virtualenv')
  " You can specify revision/branch/tag.
"  call dein#add('Shougo/deol.nvim', { 'rev': 'a1b5108fd' })

  " Required:
  call dein#end()
  call dein#save_state()
endif

" Required:
filetype plugin indent on
syntax enable

" If you want to install not installed plugins on startup.
"if dein#check_install()
"  call dein#install()
"endif

"End dein Scripts-------------------------


set number
let g:ycm_global_ycm_extra_conf = '/home/alvazir/.local/share/dein/repos/github.com/Valloric/YouCompleteMe/third_party/ycmd/cpp/ycm/.ycm_extra_conf.py'
let g:ycm_python_binary_path = 'python'
let g:jedi#completions_enabled = 0
let g:ale_virtualenv_dir_names = ['.venv']
let g:ale_fixers = {'python': ['remove_trailing_lines', 'trim_whitespace', 'add_blank_lines_for_python_control_statements', 'isort', 'autopep8', 'yapf']}
nmap <F8> <Plug>(ale_fix)

let g:ale_python_autopep8_options = '--aggressive --aggressive'

autocmd FileType python
autocmd Filetype ruby call SetPythonIndentOptions()
function SetPythonIndentOptions()
	set tabstop=4 
	set shiftwidth=4
	set softtabstop=4
	set expandtab
	set smarttab
	set backspace=indent,eol,start
	set ruler
	set showcmd
	set showmatch
	set listchars=tab:>-,trail:-,nbsp:_
	set list
endfunction
