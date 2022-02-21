import React, { FC } from 'react'
import './Image.scss'
import { BASE_URL } from '../../../utils/axios'

type Props = {
  url: string
  type?: 'absolute' | 'relative'
  className?: string
  alt?: string
}

const Image: FC<Props> = ({ url, type = 'absolute', className, alt }) => {
  return (
    <img
      src={type === 'absolute' ? url : BASE_URL + url}
      className={className}
      alt={alt}
    />
  )
}

export default Image
