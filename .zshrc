# Aliases
alias glog="git log --oneline --all --graph --decorate"
alias gatus="git status"
alias gls="git status && glog"

# Local python environment, specific for the project
alias lpe="source .venv/bin/activate"

autoload -Uz vcs_info
precmd() { vcs_info }
# Format the vcs_info_msg_0_ variable
zstyle ':vcs_info:git:*' formats '(%b)'
 
# Set up the prompt (with git branch name)
setopt PROMPT_SUBST
PROMPT='%n%f@%m%f %F{green}%1~ %F{red}${vcs_info_msg_0_}%f $ '
