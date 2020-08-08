declare DIR="$(cd "$(dirname "$0")/.." && pwd -P)"
mkdir -p "$DIR/build"

declare addon_id='persitent_editor'

cd "$DIR"

zip -r "$DIR/build/$addon_id.ankiaddon" \
  "manifest.json" \
  "__init__.py" \
  "src/"*".py" \
  "web/"* \
