set number
syntax enable
set encoding=utf-8
set relativenumber
set mouse=a
set numberwidth=1
set clipboard+=unnamedplus
set showcmd
set ruler
set showmatch
set sw=2
set laststatus=2
set noshowmode
set bg=dark
call plug#begin('~/.config/nvim/plugged')

"Temas
Plug 'morhetz/gruvbox'

"IDE
Plug 'easymotion/vim-easymotion' 
Plug 'scrooloose/nerdtree'
Plug 'christoomey/vim-tmux-navigator'
Plug 'ycm-core/YouCompleteMe'
Plug 'mattn/emmet-vim'
Plug 'mustache/vim-mustache-handlebars'
Plug 'prettier/vim-prettier', { 'do': 'yarn install' }
Plug 'vim-airline/vim-airline'
Plug 'zacanger/angr.vim'
Plug 'vim-airline/vim-airline-themes'
Plug 'mhartington/oceanic-next'
call plug#end()

let mapleader=" "
inoremap <C-h> <Left>
inoremap <C-j> <Down>
inoremap <C-k> <Up>
inoremap <C-l> <Right>
nmap <leader>w :w<CR>
nmap <leader>q :q<CR>
inoremap " ""<left>
inoremap ' ''<left>
inoremap ( ()<left>
inoremap [ []<left>
inoremap { {}<left>
inoremap {<CR> {<CR>}<ESC>O
inoremap {;<CR> {<CR>};<ESC>O
inoremap < <> <left>

let g:oceanic_next_terminal_bold = 1
let g:oceanic_next_terminal_italic = 1
let $NVIM_TUI_ENABLE_TRUE_COLOR=1
set termguicolors
" Theme
colorscheme OceanicNext


let g:gruvbox_contrast_dark='hard'


let g:EasyMotion_do_mapping = 0
nmap <Leader>s <Plug>(easymotion-overwin-f2)
nmap <Leader>n :NERDTreeFind<CR>
nmap <Leader>f :/
let g:user_emmet_leader_key=','

let g:prettier#exec_cmd_path = "~/.config/nvim/plugged/vim-prettier/node_modules/.bin/prettier"

let g:prettier#config#tab_width = '2'

" use tabs instead of spaces: true, false, or auto (use the expandtab setting).
" default: 'auto'
let g:prettier#config#use_tabs = 'false'
let g:airline_theme='angr'
let g:airline_powerline_fonts = 1 
let g:ycm_tsserver_binary_path="./node_modules/typescript/bin/tsserver"
let g:syntastic_typescript_tsc_fname = ''
set t_Co=256

highlight Normal guibg=none
highlight NonText guibg=none
