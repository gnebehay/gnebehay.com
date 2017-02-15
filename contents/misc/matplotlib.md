code: true
lang: python

# Matplotlib

## Equal axes, resizable
```
plt.gca().set_aspect('equal', adjustable='box')
```

## Register keypress function
```
plt.gcf().canvas.mpl_disconnect(plt.gcf().canvas.manager.key_press_handler_id)
plt.gcf().canvas.mpl_connect('key_press_event', onpress)
```

## Save figure
```
plt.figure(figsize=[10, 10])
plt.savefig('output.png')
```
