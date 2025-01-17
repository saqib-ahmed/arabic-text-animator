import click
import cv2
from typing import Dict, Any, Optional
from .utils.preview import LivePreview
import logging
from arabic_animations import __version__

# Set up logging
logger = logging.getLogger('arabic_animations')
handler = logging.StreamHandler()
formatter = logging.Formatter('%(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

@click.group()
def cli() -> None:
    """Arabic Animations CLI"""
    pass

@cli.command()
@click.argument('script_path', type=click.Path(exists=True))
@click.option('--preview', is_flag=True, help="Show live preview")
@click.option('--output', type=click.Path(), help="Output video path")
@click.option('-v', '--verbose', is_flag=True, help="Enable verbose output")
def render(script_path: str, preview: bool, output: Optional[str], verbose: bool) -> None:
    """Render animation from script"""
    # Set logging level based on verbosity
    logger.setLevel(logging.DEBUG if verbose else logging.INFO)

    logger.debug(f"Loading script: {script_path}")

    if preview:
        logger.debug("Starting preview...")
        preview_window = LivePreview(script_path, verbose=verbose)
        preview_window.start()
        return

    # Load scene for rendering
    namespace = {}
    with open(script_path) as f:
        script_content = f.read()
        logger.debug(f"Script content:\n{script_content}")
        exec(script_content, namespace)

    scene = namespace.get('scene')
    if not scene:
        click.echo("Error: Script must define a 'scene' object")
        return

    if output:
        logger.info(f"Rendering to {output}...")
        # Render to video file
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(output, fourcc, scene.fps,
                            (scene.width, scene.height))

        duration = scene.duration
        total_frames = int(duration * scene.fps)

        with click.progressbar(range(total_frames), label='Rendering') as frames:
            for t in frames:
                frame = scene.render_frame(t / scene.fps)
                out.write(cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR))

        out.release()
        logger.info("Done!")

@cli.command()
def docs() -> None:
    """Start the documentation server"""
    import subprocess
    subprocess.run(["mkdocs", "serve"])