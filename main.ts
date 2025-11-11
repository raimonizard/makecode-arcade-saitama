scene.setBackgroundImage(assets.image`bosc`)
let saitama = sprites.create(assets.image`saitama`, SpriteKind.Player)
controller.moveSprite(saitama)
animation.runImageAnimation(
saitama,
assets.animation`moviment_saitama`,
200,
true
)
forever(function () {
    music.play(music.createSong(assets.song`theme`), music.PlaybackMode.UntilDone)
})
