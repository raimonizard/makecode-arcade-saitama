scene.set_background_image(assets.image("""
    bosc
    """))
saitama = sprites.create(assets.image("""
    saitama
    """), SpriteKind.player)
controller.move_sprite(saitama)
animation.run_image_animation(saitama,
    assets.animation("""
        moviment_saitama
        """),
    200,
    True)

def on_forever():
    music.play(music.create_song(assets.song("""
            theme
            """)),
        music.PlaybackMode.UNTIL_DONE)
forever(on_forever)
