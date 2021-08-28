#!/usr/bin/env bash

# displays utc datetime before every console write
exec &> >( while IFS= read -r line; do printf '%s %s\n' "$(date -u +"%Y-%m-%dT%H:%M:%S.%sZ")" "$line"; done )


main() {
    # printenv
    echo "Hello, $1"
    aws sts get-caller-identity
}

main "World"
