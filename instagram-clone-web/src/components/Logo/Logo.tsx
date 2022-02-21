import React, { FC } from 'react'
import Image from '../Widgets/Image'

type Props = {
  className?: string
}

const Logo: FC<Props> = ({ className }) => {
  return (
    <Image
      url='https://www.meilleure-innovation.com/wp-content/uploads/2021/05/logo-instagram-png-transparent.png'
      alt='Instagram'
      className={className}
    />
  )
}

export default Logo
