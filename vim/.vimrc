
" ------------------------- Pathogen ------------------------------------------------- "
execute pathogen#infect()

" ------------------------- Pathogen ------------------------------------------------- "
autocmd VimEnter * NERDTree

" ------------------------- Load startup files --------------------------------------- "
source ~/.vim/startup/color.vim
source ~/.vim/startup/settings.vim

" ------------------------- Filetype stuff ------------------------------------------- "
filetype plugin on
filetype indent on

" ------------------------- Keyboard mappings ---------------------------------------- "
let mapleader=","
nmap <silent> <leader>ev :e $MYVIMRC<CR>
nmap <silent> <leader>sv :so $MYVIMRC<CR>

" Start interactive EasyAlign in visual mode (e.g. vip<Enter>)
vmap <Enter> <Plug>(EasyAlign)

" Start interactive EasyAlign for a motion/text object (e.g. gaip)
nmap ga <Plug>(EasyAlign)


" powerline settings
set rtp+=~/.vim/bundle/powerline/powerline/bindings/vim





