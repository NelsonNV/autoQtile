" neovim config 0
set number
set mouse=a
set encoding=utf-8
set autoindent
set ruler


call plug#begin()
Plug 'vim-airline/vim-airline' " line de estado
Plug 'eslint/eslint'
Plug 'ryanoasis/vim-devicons' " iconos para nerdTree
Plug 'vim-python/python-syntax' " resaltado de sintanxy python
Plug 'neoclide/coc.nvim', {'branch': 'release'} "Resaltado de errores https://vimawesome.com/plugin/coc-nvim
Plug 'preservim/nerdtree' " rama o explorador de archivo
Plug 'joshdick/onedark.vim' "thema

" bar thema https://vimawesome.com/plugin/barbar-nvim
Plug 'kyazdani42/nvim-web-devicons'
Plug 'romgrk/barbar.nvim'
"ajustes de git
Plug 'mhinz/vim-signify' "cambios en lineas
Plug 'apzelos/blamer.nvim' "fecha o info del commint de la linea
Plug 'xuyuanp/nerdtree-git-plugin' " vista de cambios de git a la ramas
Plug 'tpope/vim-fugitive' "usar comandos de git https://vimawesome.com/plugin/fugitive-vim

Plug 'vim-scripts/sudo.vim' "https://vimawesome.com/plugin/sudo-vim
Plug 'manasthakur/vim-commentor' "Commentar linea rapido


call plug#end()

" config plugini 0
" coc.nvim = https://github.com/neoclide/coc-python 
let g:python_highlight_all = 1 " activar resaltado highlight
" abrir neerd tree rapido
nnoremap <C-n> :NERDTreeToggle<cr>
" guardado rapido 
nnoremap <C-s> :w<cr>
"nmap :W :w
" abrir terminal
nnoremap <C-ñ> :terminal<cr>

"gcc commentar line

" ajustes blamer 
let g:blamer_enabled = 1 "que se desactive cada vez que no esta en un git
let g:blamer_delay = 500 "Cuanto milisegundos se demora
let g:blamer_prefix = ' <- ' " prefijo al mostara un mensaje


" thema de neovim
colorscheme onedark
